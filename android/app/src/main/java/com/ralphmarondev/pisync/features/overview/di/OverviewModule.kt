package com.ralphmarondev.pisync.features.overview.di

import com.ralphmarondev.pisync.features.overview.data.network.DoorApiService
import com.ralphmarondev.pisync.features.overview.data.network.UserDetailApiService
import com.ralphmarondev.pisync.features.overview.data.repositories.OverviewRepositoryImpl
import com.ralphmarondev.pisync.features.overview.data.repositories.UserDetailRepositoryImpl
import com.ralphmarondev.pisync.features.overview.domain.repositories.OverviewRepository
import com.ralphmarondev.pisync.features.overview.domain.repositories.UserDetailRepostory
import com.ralphmarondev.pisync.features.overview.domain.usecases.CloseDoorByIdUseCase
import com.ralphmarondev.pisync.features.overview.domain.usecases.GetDoorsByUsernameUseCase
import com.ralphmarondev.pisync.features.overview.domain.usecases.GetUserDetailByUsernameUseCase
import com.ralphmarondev.pisync.features.overview.domain.usecases.OpenDoorByIdUseCase
import com.ralphmarondev.pisync.features.overview.presentation.OverviewViewModel
import org.koin.androidx.viewmodel.dsl.viewModelOf
import org.koin.core.module.dsl.factoryOf
import org.koin.dsl.module
import retrofit2.Retrofit

val overviewModule = module {
    single { get<Retrofit>().create(DoorApiService::class.java) }
    single { get<Retrofit>().create(UserDetailApiService::class.java) }

    single<OverviewRepository> { OverviewRepositoryImpl(get()) }
    single<UserDetailRepostory> { UserDetailRepositoryImpl(get()) }

    factoryOf(::GetDoorsByUsernameUseCase)
    factoryOf(::CloseDoorByIdUseCase)
    factoryOf(::OpenDoorByIdUseCase)

    factoryOf(::GetUserDetailByUsernameUseCase)

    viewModelOf(::OverviewViewModel)
}