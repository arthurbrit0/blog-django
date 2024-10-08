# Generated by Django 4.2 on 2024-09-20 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_author_profile_autor_rename_date_profile_data_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagem', models.FileField(blank=True, null=True, upload_to='image')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('imagem', models.FileField(blank=True, null=True, upload_to='image')),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Rascunho', 'Rascunho'), ('Desabilitado', 'Desabilitado')], default='Ativo', max_length=100)),
                ('view', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.categoria')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes_user', to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Post',
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Like', 'Like'), ('Comentario', 'Comentario')], max_length=100)),
                ('visto', models.BooleanField(default=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Bookmark',
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_user', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('resposta', models.TextField(blank=True, null=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.post')),
            ],
            options={
                'verbose_name_plural': 'Comentario',
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Bookmark',
                'ordering': ['-data'],
            },
        ),
    ]
