# Generated by Django 4.0.4 on 2022-05-21 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blurb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blurbHeader', models.CharField(max_length=100)),
                ('blurb', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.page')),
            ],
        ),
        migrations.CreateModel(
            name='BlurbPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blurb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.blurb')),
            ],
        ),
        migrations.AddField(
            model_name='blurb',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.page'),
        ),
    ]