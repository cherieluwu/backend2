# Generated by Django 5.1.1 on 2024-10-22 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbiblioteca', '0002_libros_usuarios_remove_libro_autor_delete_usuario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libros',
            old_name='autor',
            new_name='id_autor',
        ),
        migrations.AlterField(
            model_name='autor',
            name='estado',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=models.TextField(max_length=99, verbose_name='Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='libros',
            name='idioma',
            field=models.CharField(choices=[('0', 'Español'), ('1', 'Inglés'), ('2', 'Portugués')], max_length=20, verbose_name='Idioma'),
        ),
    ]
