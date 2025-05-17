package com.ralphmarondev.pisync.features.app_theme.di

import com.ralphmarondev.pisync.features.app_theme.presentation.AppThemeViewModel
import org.koin.androidx.viewmodel.dsl.viewModelOf
import org.koin.dsl.module

val appThemeModule = module {
    viewModelOf(::AppThemeViewModel)
}