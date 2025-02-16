package com.ralphmarondev.pisync.core.data.network

import com.ralphmarondev.pisync.core.domain.Result
import com.ralphmarondev.pisync.features.auth.domain.model.User
import com.ralphmarondev.pisync.features.history.domain.model.DoorLog
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST

interface ApiService {
    @POST("login/")
    suspend fun login(@Body user: User): Result

    @GET("history/")
    suspend fun getHistory(): List<DoorLog>
}