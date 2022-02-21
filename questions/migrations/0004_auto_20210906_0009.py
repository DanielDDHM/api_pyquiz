# Generated by Django 3.2.6 on 2021-09-06 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(choices=[('1', 'Primeira Resposta'), ('2', 'Segunda Resposta'), ('3', 'Terceira Resposta')], max_length=1, verbose_name='Resposta Correta'),
        ),
        migrations.AlterField(
            model_name='question',
            name='first_answer',
            field=models.CharField(max_length=255, null=True, verbose_name='1ª Resposta'),
        ),
        migrations.AlterField(
            model_name='question',
            name='second_answer',
            field=models.CharField(max_length=255, null=True, verbose_name='2ª Resposta'),
        ),
        migrations.AlterField(
            model_name='question',
            name='third_answer',
            field=models.CharField(max_length=255, null=True, verbose_name='3ª Resposta'),
        ),
    ]
