package com.ralphmarondev.pisync.features.overview.di

import com.ralphmarondev.pisync.features.overview.presentation.OverviewViewModel
import org.koin.androidx.viewmodel.dsl.viewModelOf
import org.koin.dsl.module

val overviewModule = module {
    viewModelOf(::OverviewViewModel)
}