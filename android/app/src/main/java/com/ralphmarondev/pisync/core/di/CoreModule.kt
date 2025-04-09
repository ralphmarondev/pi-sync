package com.ralphmarondev.pisync.core.di

import com.ralphmarondev.pisync.core.data.local.preferences.AppPreferences
import com.ralphmarondev.pisync.core.util.ThemeState
import org.koin.core.module.dsl.singleOf
import org.koin.dsl.module
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

//const val IP_ADDRESS = "192.168.100.96" // on jam
const val IP_ADDRESS = "192.168.68.132" // on boarding
const val BASE_URL = "http://$IP_ADDRESS:8000/api/"

val coreModule = module {
    singleOf(::AppPreferences)
    singleOf(::ThemeState)

    single {
        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
    }
}