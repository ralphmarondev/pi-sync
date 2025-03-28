package com.ralphmarondev.pisync.features.history.di

import com.ralphmarondev.pisync.features.history.presentation.HistoryViewModel
import org.koin.androidx.viewmodel.dsl.viewModelOf
import org.koin.dsl.module

val historyModule = module {
    viewModelOf(::HistoryViewModel)
}