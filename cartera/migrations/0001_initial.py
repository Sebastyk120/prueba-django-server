# Generated by Django 5.0.7 on 2024-08-03 16:19

import django.core.validators
import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comercial', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CotizacionEtnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semana', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(56)], verbose_name='Semana')),
                ('trm_cotizacion', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='TRM Cotizacion')),
                ('precio_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$FOB')),
                ('comi_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com FOB')),
                ('precio_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DXB')),
                ('comi_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DXB')),
                ('precio_doh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DOH')),
                ('comi_doh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DOH')),
                ('precio_bah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$BAH')),
                ('comi_bah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com BAH')),
                ('precio_kwi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$KWI')),
                ('comi_kwi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com KWI')),
                ('precio_ruh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$RUH')),
                ('comi_ruh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com RUH')),
                ('precio_jed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$JED')),
                ('comi_jed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com JED')),
                ('precio_svo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$SVO')),
                ('comi_svo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com SVO')),
                ('precio_lhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$LHR')),
                ('comi_lhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com LHR')),
                ('precio_ams', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$AMS')),
                ('comi_ams', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com AMS')),
                ('precio_mad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MAD')),
                ('comi_mad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MAD')),
                ('precio_mxp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MXP')),
                ('comi_mxp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MXP')),
                ('precio_vko', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$VKO')),
                ('comi_vko', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com VKO')),
                ('presentacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.presentacion')),
            ],
        ),
        migrations.CreateModel(
            name='CotizacionFieldex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semana', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(56)], verbose_name='Semana')),
                ('trm_cotizacion', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='TRM Cotizacion')),
                ('precio_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$FOB')),
                ('comi_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com FOB')),
                ('precio_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DXB')),
                ('comi_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DXB')),
                ('precio_doh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DOH')),
                ('comi_doh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DOH')),
                ('precio_bah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$BAH')),
                ('comi_bah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com BAH')),
                ('precio_kwi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$KWI')),
                ('comi_kwi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com KWI')),
                ('precio_ruh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$RUH')),
                ('comi_ruh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com RUH')),
                ('precio_jed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$JED')),
                ('comi_jed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com JED')),
                ('precio_svo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$SVO')),
                ('comi_svo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com SVO')),
                ('precio_lhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$LHR')),
                ('comi_lhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com LHR')),
                ('precio_ams', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$AMS')),
                ('comi_ams', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com AMS')),
                ('precio_mad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MAD')),
                ('comi_mad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MAD')),
                ('precio_mxp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MXP')),
                ('comi_mxp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MXP')),
                ('precio_vko', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$VKO')),
                ('comi_vko', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com VKO')),
                ('presentacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.presentacion')),
            ],
        ),
        migrations.CreateModel(
            name='CotizacionJuan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semana', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(56)], verbose_name='Semana')),
                ('trm_cotizacion', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='TRM Cotizacion')),
                ('precio_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$FOB')),
                ('comi_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com FOB')),
                ('precio_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DXB')),
                ('comi_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DXB')),
                ('precio_doh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DOH')),
                ('comi_doh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DOH')),
                ('precio_bah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$BAH')),
                ('comi_bah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com BAH')),
                ('precio_kwi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$KWI')),
                ('comi_kwi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com KWI')),
                ('precio_ruh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$RUH')),
                ('comi_ruh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com RUH')),
                ('precio_jed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$JED')),
                ('comi_jed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com JED')),
                ('precio_svo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$SVO')),
                ('comi_svo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com SVO')),
                ('precio_lhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$LHR')),
                ('comi_lhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com LHR')),
                ('precio_ams', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$AMS')),
                ('comi_ams', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com AMS')),
                ('precio_mad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MAD')),
                ('comi_mad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MAD')),
                ('precio_mxp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MXP')),
                ('comi_mxp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MXP')),
                ('precio_vko', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$VKO')),
                ('comi_vko', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com VKO')),
                ('presentacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercial.presentacion')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalCotizacionEtnico',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('semana', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(56)], verbose_name='Semana')),
                ('trm_cotizacion', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='TRM Cotizacion')),
                ('precio_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$FOB')),
                ('comi_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com FOB')),
                ('precio_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DXB')),
                ('comi_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DXB')),
                ('precio_doh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DOH')),
                ('comi_doh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DOH')),
                ('precio_bah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$BAH')),
                ('comi_bah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com BAH')),
                ('precio_kwi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$KWI')),
                ('comi_kwi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com KWI')),
                ('precio_ruh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$RUH')),
                ('comi_ruh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com RUH')),
                ('precio_jed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$JED')),
                ('comi_jed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com JED')),
                ('precio_svo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$SVO')),
                ('comi_svo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com SVO')),
                ('precio_lhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$LHR')),
                ('comi_lhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com LHR')),
                ('precio_ams', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$AMS')),
                ('comi_ams', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com AMS')),
                ('precio_mad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MAD')),
                ('comi_mad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MAD')),
                ('precio_mxp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MXP')),
                ('comi_mxp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MXP')),
                ('precio_vko', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$VKO')),
                ('comi_vko', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com VKO')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('presentacion', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='comercial.presentacion')),
            ],
            options={
                'verbose_name': 'historical cotizacion etnico',
                'verbose_name_plural': 'historical cotizacion etnicos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCotizacionFieldex',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('semana', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(56)], verbose_name='Semana')),
                ('trm_cotizacion', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='TRM Cotizacion')),
                ('precio_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$FOB')),
                ('comi_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com FOB')),
                ('precio_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DXB')),
                ('comi_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DXB')),
                ('precio_doh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DOH')),
                ('comi_doh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DOH')),
                ('precio_bah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$BAH')),
                ('comi_bah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com BAH')),
                ('precio_kwi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$KWI')),
                ('comi_kwi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com KWI')),
                ('precio_ruh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$RUH')),
                ('comi_ruh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com RUH')),
                ('precio_jed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$JED')),
                ('comi_jed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com JED')),
                ('precio_svo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$SVO')),
                ('comi_svo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com SVO')),
                ('precio_lhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$LHR')),
                ('comi_lhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com LHR')),
                ('precio_ams', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$AMS')),
                ('comi_ams', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com AMS')),
                ('precio_mad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MAD')),
                ('comi_mad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MAD')),
                ('precio_mxp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MXP')),
                ('comi_mxp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MXP')),
                ('precio_vko', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$VKO')),
                ('comi_vko', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com VKO')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('presentacion', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='comercial.presentacion')),
            ],
            options={
                'verbose_name': 'historical cotizacion fieldex',
                'verbose_name_plural': 'historical cotizacion fieldexs',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCotizacionJuan',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('semana', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(56)], verbose_name='Semana')),
                ('trm_cotizacion', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='TRM Cotizacion')),
                ('precio_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$FOB')),
                ('comi_fob', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com FOB')),
                ('precio_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DXB')),
                ('comi_dxb', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DXB')),
                ('precio_doh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$DOH')),
                ('comi_doh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com DOH')),
                ('precio_bah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$BAH')),
                ('comi_bah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com BAH')),
                ('precio_kwi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$KWI')),
                ('comi_kwi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com KWI')),
                ('precio_ruh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$RUH')),
                ('comi_ruh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com RUH')),
                ('precio_jed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$JED')),
                ('comi_jed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com JED')),
                ('precio_svo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$SVO')),
                ('comi_svo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com SVO')),
                ('precio_lhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$LHR')),
                ('comi_lhr', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com LHR')),
                ('precio_ams', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$AMS')),
                ('comi_ams', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com AMS')),
                ('precio_mad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MAD')),
                ('comi_mad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MAD')),
                ('precio_mxp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$MXP')),
                ('comi_mxp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com MXP')),
                ('precio_vko', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='$VKO')),
                ('comi_vko', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Com VKO')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('presentacion', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='comercial.presentacion')),
            ],
            options={
                'verbose_name': 'historical cotizacion juan',
                'verbose_name_plural': 'historical cotizacion juans',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
