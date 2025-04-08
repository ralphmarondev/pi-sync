package com.ralphmarondev.pisync.features.overview.data.models

data class UserDetailResponse(
    val success: Boolean,
    val message: String,
    val user: UserInfo
)

data class UserInfo(
    val id: Int,
    val email: String,
    val username: String,
    val hint_password: String,
    val first_name: String,
    val last_name: String,
    val gender: String,
    val is_superuser: Boolean,
    val image: String?
)