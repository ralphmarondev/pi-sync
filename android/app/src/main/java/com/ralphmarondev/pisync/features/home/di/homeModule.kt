package com.ralphmarondev.pisync.features.home.di

import com.ralphmarondev.pisync.features.home.presentation.HomeViewModel
import org.koin.androidx.viewmodel.dsl.viewModelOf
import org.koin.dsl.module

val homeModule = module {
    viewModelOf(::HomeViewModel)
}