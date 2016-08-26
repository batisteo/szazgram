from django.db import models


class Illustration(models.Model):
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title

    def save_image(self, url):
        try:
            img = requests.get(url, timeout=10)
        except (ConnectionError, Timeout) as e:
            return False
        picture = File(open(img.raw))
        # Resize here
        try:
            self.image.save(os.path.basename(url), picture)
        except:  #Not an image
            return False
        return self
