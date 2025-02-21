package com.ralphmarondev.pisync.features.auth.domain.repository

import com.ralphmarondev.pisync.core.domain.Result
import com.ralphmarondev.pisync.features.auth.domain.model.PasswordHintResponse
import com.ralphmarondev.pisync.features.auth.domain.model.User

interface AuthRepository {
    suspend fun login(user: User): Result
    suspend fun updateIpAddress(ipAddress: String): Result
    suspend fun getPasswordHint(username: String): PasswordHintResponse
}