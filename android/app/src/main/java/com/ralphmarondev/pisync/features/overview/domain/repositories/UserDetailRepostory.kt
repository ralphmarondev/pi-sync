package com.ralphmarondev.pisync.features.overview.domain.repositories

import com.ralphmarondev.pisync.features.overview.domain.model.UserDetail

interface UserDetailRepostory {
    suspend fun getUserDetailByUsername(username: String): UserDetail
}