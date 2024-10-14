package com.ralphmarondev.pisync.features.auth.domain.repository

import com.ralphmarondev.pisync.core.model.LoginRequest
import com.ralphmarondev.pisync.core.model.LoginResponse

interface AuthRepository {
    suspend fun login(loginRequest: LoginRequest): LoginResponse
}