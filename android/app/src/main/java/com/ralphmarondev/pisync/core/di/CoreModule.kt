package com.ralphmarondev.pisync.core.di

import android.content.Context
import androidx.room.Room
import com.ralphmarondev.pisync.core.data.local.database.AppDatabase
import com.ralphmarondev.pisync.core.data.local.preferences.AppPreferences
import com.ralphmarondev.pisync.core.data.repositories.RoomRepositoryImpl
import com.ralphmarondev.pisync.core.domain.repositories.RoomRepository
import com.ralphmarondev.pisync.core.domain.usecases.DeleteAllRoomsUseCase
import com.ralphmarondev.pisync.core.domain.usecases.GetAllRoomsUseCase
import com.ralphmarondev.pisync.core.domain.usecases.SaveRoomUseCase
import com.ralphmarondev.pisync.core.util.ThemeState
import org.koin.core.module.dsl.factoryOf
import org.koin.core.module.dsl.singleOf
import org.koin.dsl.module
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

//const val IP_ADDRESS = "192.168.100.96" // on jam
//const val IP_ADDRESS = "192.168.68.132" // on boarding
//const val IP_ADDRESS = "192.168.1.99" // on triesha mae boarding
const val IP_ADDRESS = "192.168.68.116"
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

    single {
        Room.databaseBuilder(
            get<Context>(),
            AppDatabase::class.java,
            AppDatabase.NAME
        ).build()
    }
    single { get<AppDatabase>().roomDao() }
    single<RoomRepository> { RoomRepositoryImpl(get()) }

    factoryOf(::GetAllRoomsUseCase)
    factoryOf(::SaveRoomUseCase)
    factoryOf(::DeleteAllRoomsUseCase)
}