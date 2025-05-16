package com.ralphmarondev.pisync.features.overview.domain.model

data class UserDetail(
    val id: Int = 0,
    val firstName: String,
    val lastName: String,
    val username: String,
    val email: String,
    val gender: String,
    val hintPassword: String,
    val isSuperUser: Boolean,
    val image: String?
)
