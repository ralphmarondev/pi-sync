package com.ralphmarondev.pisync.features.auth.data.repositories

import com.ralphmarondev.pisync.features.auth.data.network.AuthApiService
import com.ralphmarondev.pisync.features.auth.domain.model.LoginRequest
import com.ralphmarondev.pisync.features.auth.domain.repositories.AuthRepository

class AuthRepositoryImpl(
    private val api: AuthApiService
) : AuthRepository {
    override suspend fun login(username: String, password: String): Boolean {
        val response = api.login(request = LoginRequest(username = username, password = password))
        return response.success
    }
}