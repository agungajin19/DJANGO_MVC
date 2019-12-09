from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length=20)
    species = models.CharField(max_length=20, default='')
    berat = models.IntegerField(default=0)
    umur = models.IntegerField(default=0)

    def __str__(self):
        return self.nama

class Kandang(models.Model):
    nama = models.CharField(max_length=20)
    isi_kandang = models.IntegerField(default=0)
    luas_kandang = models.IntegerField(default=0)

    def __str__(self):
        return self.nama

class Penjaga(models.Model):
    nama = models.CharField(max_length=40)
    nomor_telepon = models.CharField(max_length=15, default='')
    jadwal_jaga = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.nama

class Pengunjung(models.Model):
    nama = models.CharField(max_length=40)
    nomor_telepon = models.CharField(max_length=15, default='')
    hari_berkunjung = models.CharField(max_length=40, default='')
    
    def __str__(self):
        return self.nama


