# Generated by Django 4.2 on 2023-10-15 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activated', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text="The object's creation date/time", null=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now_add=True, help_text="The object's last update date/time", null=True, verbose_name='updated on')),
                ('token', models.CharField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('number_of_uses', models.IntegerField(default=0)),
                ('relatedModel', models.CharField(blank=True, max_length=255, null=True)),
                ('relatedModelId', models.IntegerField(blank=True, null=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='token_profile', to='profiles.profile')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
                'db_table': 'token',
            },
        ),
    ]
