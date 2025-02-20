package com.ralphmarondev.pisync.features.home.domain.model

data class User(
    val id: Int,
    val firstName: String,
    val lastName: String,
    val username: String,
    val password: String
)