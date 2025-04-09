package com.ralphmarondev.pisync.features.history.di

import com.ralphmarondev.pisync.features.history.data.network.HistoryApiService
import com.ralphmarondev.pisync.features.history.data.repositories.HistoryRepositoryImpl
import com.ralphmarondev.pisync.features.history.domain.repositories.HistoryRepository
import com.ralphmarondev.pisync.features.history.domain.usecases.GetHistoryByRoomIdUseCase
import com.ralphmarondev.pisync.features.history.presentation.HistoryViewModel
import org.koin.androidx.viewmodel.dsl.viewModelOf
import org.koin.core.module.dsl.factoryOf
import org.koin.dsl.module
import retrofit2.Retrofit

val historyModule = module {
    single { get<Retrofit>().create(HistoryApiService::class.java) }
    single<HistoryRepository> { HistoryRepositoryImpl(get()) }

    factoryOf(::GetHistoryByRoomIdUseCase)

    viewModelOf(::HistoryViewModel)
}