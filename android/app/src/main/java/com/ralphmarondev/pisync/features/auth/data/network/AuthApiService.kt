package com.ralphmarondev.pisync.features.auth.data.network

import com.ralphmarondev.pisync.features.auth.domain.model.LoginRequest
import com.ralphmarondev.pisync.features.auth.domain.model.LoginResponse
import retrofit2.http.Body
import retrofit2.http.POST

interface AuthApiService {

    @POST("login/")
    suspend fun login(
        @Body request: LoginRequest
    ): LoginResponse
}