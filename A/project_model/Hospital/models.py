from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length=50)
    nomor_telepon = models. CharField(max_length=15, default='')
    bidang = models.CharField(max_length=30, default='')
    jadwal_praktek = models.DateTimeField('Jadwal Praktek')

    def __str__(self):
        return self.nama

class Pasien(models.Model):
    nama = models.CharField(max_length=50)
    nomor_telepon = models.CharField(max_length=15, default='')
    alamat = models.CharField(max_length=100, default='')
    keluhan = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.nama

class Resep(models.Model):
    nama = models.CharField(max_length=100)
    total_harga = models.IntegerField(default=0)
    kumpulan_obat = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nama

class Obat(models.Model):
    nama = models.CharField(max_length=100)
    kandungan = models.CharField(max_length=200, default='')
    khasiat = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.nama

