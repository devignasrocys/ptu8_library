from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid  # sukurs unikalu id
# vertimu _ funkcija vers teksta i kitas kalbas
# cia dedamos tik tai klases kuriu modelius naudosim duombazem. Tik duomenys
# modelis tiktais vienaskaita
# Create your models here.
class Genre(models.Model):
    name = models.CharField(_("name"), max_length=50) #

    def __str__(self) -> str:
        return self.name
    

class Author(models.Model):
    first_name = models.CharField(_("first name"), max_length=100, db_index=True)
    last_name = models.CharField(_("last name"), max_length=100, db_index=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    # aprasomojo klase modeliui, kurioje nurodome papildomas instrukcijas
    # tarkim ordering ir pns
    class Meta:
        ordering = ["last_name", "first_name"]


class Book(models.Model):
    title = models.CharField(_("title"), max_length=255, db_index=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT, # ka daryti istrynus author is db
        related_name="books", # kaip pasieksim knygas is autoriaus
        verbose_name=_("author") 
    )
    sumary = models.TextField(_("sumary"), max_length=4000, null=True, blank=True)
    genre = models.ManyToManyField(
        Genre,
        help_text=_("select genre(s) for this book"),
        verbose_name=_("genre(s)")
    )

    def __str__(self) -> str:
        return f"{self.author} - {self.title}"
    
    class Meta:
        ordering = ["title"]


class BookInstance(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, default=uuid.uuid4, help_text=_("Unique ID for book copy"))
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, # cascade jeigu istrins knyga visos jos kopijos issitrins
        related_name="book_instances",
        verbose_name=_("book")
        ) 
    due_back = models.DateField(_("due back"), null=True, db_index=True)

    LOAN_STATUS = (
        ("m", _("managed")),
        ("r", _("reserved")),
        ("t", _("taken")),
        ("a", _("available")),
        ("u", _("unavailable")),
    )

    status = models.CharField(_("status"), max_length=1, choices=LOAN_STATUS, default="a")

    def __str__(self) -> str:
        return f"{self.id} {self.book}"
    
    class Meta():
        ordering = ["due_back"]
