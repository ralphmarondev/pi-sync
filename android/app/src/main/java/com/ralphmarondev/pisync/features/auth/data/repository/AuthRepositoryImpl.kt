package com.ralphmarondev.pisync.features.auth.data.repository

import com.ralphmarondev.pisync.core.data.network.RetrofitInstance
import com.ralphmarondev.pisync.core.data.preferences.AppPreferences
import com.ralphmarondev.pisync.core.domain.Result
import com.ralphmarondev.pisync.core.model.LoginRequest
import com.ralphmarondev.pisync.features.auth.domain.repository.AuthRepository

class AuthRepositoryImpl(
    private val preferences: AppPreferences
) : AuthRepository {
    override suspend fun login(loginRequest: LoginRequest): Result {
        return RetrofitInstance.api.login(loginRequest)
    }

    override suspend fun updateIpAddress(ipAddress: String): Result {
        return try {
            preferences.saveIpAddress(ipAddress)
            Result(success = true, message = "Success")
        } catch (e: Exception) {
            Result(success = false, message = e.message)
        }
    }
}