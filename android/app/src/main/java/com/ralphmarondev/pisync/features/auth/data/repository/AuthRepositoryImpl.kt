package com.ralphmarondev.pisync.features.auth.data.repository

import com.ralphmarondev.pisync.core.data.network.RetrofitInstance
import com.ralphmarondev.pisync.core.model.LoginRequest
import com.ralphmarondev.pisync.core.model.LoginResponse
import com.ralphmarondev.pisync.features.auth.domain.repository.AuthRepository

class AuthRepositoryImpl : AuthRepository {
    override suspend fun login(loginRequest: LoginRequest): LoginResponse {
        return RetrofitInstance.api.login(loginRequest)
    }
}