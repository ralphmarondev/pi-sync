package com.ralphmarondev.pisync.core.data.network

import com.ralphmarondev.pisync.core.model.LoginRequest
import com.ralphmarondev.pisync.core.model.LoginResponse
import retrofit2.http.Body
import retrofit2.http.POST

interface ApiService {
    @POST("auth/login/")
    suspend fun login(@Body loginRequest: LoginRequest): LoginResponse
}