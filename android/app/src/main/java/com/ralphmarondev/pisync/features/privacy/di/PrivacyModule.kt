package com.ralphmarondev.pisync.features.privacy.di

import PrivacyViewModel
import com.ralphmarondev.pisync.features.privacy.data.network.PrivacyApiService
import org.koin.androidx.viewmodel.dsl.viewModelOf
import org.koin.dsl.module
import retrofit2.Retrofit

val privacyModule = module {
    single { get<Retrofit>().create(PrivacyApiService::class.java) }

    viewModelOf(::PrivacyViewModel)
}