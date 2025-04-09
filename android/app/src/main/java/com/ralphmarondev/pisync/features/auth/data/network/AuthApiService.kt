package com.ralphmarondev.pisync.features.auth.data.network

import com.ralphmarondev.pisync.features.auth.data.model.PasswordHintResponse
import com.ralphmarondev.pisync.features.auth.domain.model.LoginRequest
import com.ralphmarondev.pisync.features.auth.domain.model.LoginResponse
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Path

interface AuthApiService {

    @POST("login/")
    suspend fun login(
        @Body request: LoginRequest
    ): LoginResponse

    @GET("user/password-hint/{username}/")
    suspend fun forgotPassword(
        @Path("username") username: String
    ): PasswordHintResponse
}