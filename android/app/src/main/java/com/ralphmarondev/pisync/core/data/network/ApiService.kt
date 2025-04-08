package com.ralphmarondev.pisync.core.data.network

import com.ralphmarondev.pisync.core.domain.model.LoginResult
import com.ralphmarondev.pisync.core.domain.model.User
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST

interface ApiService {

    @POST("login/")
    suspend fun login(@Body user: User): LoginResult

    @GET("get-password-hint-by-username/")
    suspend fun getPasswordHintByUsername(
        username: String
    ): String
}