package com.ralphmarondev.pisync.features.auth.di

import com.ralphmarondev.pisync.features.auth.data.network.AuthApiService
import com.ralphmarondev.pisync.features.auth.data.repositories.AuthRepositoryImpl
import com.ralphmarondev.pisync.features.auth.domain.repositories.AuthRepository
import com.ralphmarondev.pisync.features.auth.domain.usecases.ForgotPasswordUseCase
import com.ralphmarondev.pisync.features.auth.domain.usecases.LoginUseCase
import com.ralphmarondev.pisync.features.auth.presentation.login.LoginViewModel
import org.koin.androidx.viewmodel.dsl.viewModelOf
import org.koin.core.module.dsl.factoryOf
import org.koin.dsl.module
import retrofit2.Retrofit

val authModule = module {
    single { get<Retrofit>().create(AuthApiService::class.java) }
    single<AuthRepository> { AuthRepositoryImpl(get()) }

    factoryOf(::LoginUseCase)
    factoryOf(::ForgotPasswordUseCase)

    viewModelOf(::LoginViewModel)
}