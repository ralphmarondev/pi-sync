package com.ralphmarondev.pisync.features.auth.domain.repository

import com.ralphmarondev.pisync.core.domain.Result
import com.ralphmarondev.pisync.core.model.LoginRequest

interface AuthRepository {
    suspend fun login(loginRequest: LoginRequest): Result
    suspend fun updateIpAddress(ipAddress: String): Result
}