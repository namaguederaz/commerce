from django.contrib.auth.models import AbstractUser
from django.db import models

# each time you change anything in auctions/models.py, you’ll need to first 
# run python manage.py makemigrations and then python manage.py migrate to 
# migrate those changes to your database.
class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.id}: {self.username}"


# one for auction listings
# title for the listing, a text-based description, and what the starting bid should be
class Auction(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=280)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
    image = models.TextField(default="https://www.teknozeka.com/wp-content/uploads/2020/03/wp-header-logo-33.png")

    def __str__(self):
        return f"{self.title}"

# one for bids
class Bid(models.Model):
    offer = models.DecimalField(max_digits=10, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    product = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="product")

    def __str__(self):
        return f"{self.bidder} offered {self.offer} for {self.product}"

# one for comments made on auction listings
class Comment(models.Model):
    comentator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comentator")
    comment = models.CharField(max_length=280)
    subject = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="item")

    def __str__(self):
        return f"{self.comentator} posted on {self.subject}"