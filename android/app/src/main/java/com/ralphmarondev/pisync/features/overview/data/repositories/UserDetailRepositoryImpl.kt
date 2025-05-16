package com.ralphmarondev.pisync.features.overview.data.repositories

import com.ralphmarondev.pisync.features.overview.data.network.UserDetailApiService
import com.ralphmarondev.pisync.features.overview.domain.model.UserDetail
import com.ralphmarondev.pisync.features.overview.domain.repositories.UserDetailRepostory

class UserDetailRepositoryImpl(
    private val api: UserDetailApiService
) : UserDetailRepostory {
    override suspend fun getUserDetailByUsername(username: String): UserDetail {
        val response = api.getUserDetailByUsername(username)
        val user = response.user

        return UserDetail(
            id = user.id,
            firstName = user.first_name,
            lastName = user.last_name,
            username = user.username,
            email = user.email,
            gender = user.gender,
            hintPassword = user.hint_password,
            isSuperUser = user.is_superuser,
            image = user.image
        )
    }
}