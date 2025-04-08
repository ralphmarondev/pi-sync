package com.ralphmarondev.pisync.features.overview.domain.usecases

import com.ralphmarondev.pisync.features.overview.domain.repositories.UserDetailRepostory

class GetUserDetailByUsernameUseCase(
    private val repostory: UserDetailRepostory
) {
    suspend operator fun invoke(username: String) = repostory.getUserDetailByUsername(username)
}