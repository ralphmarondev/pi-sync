package com.ralphmarondev.pisync.features.home.domain.model

data class DoorActionRequest(
    val doorId: Int = 1,
    val username: String,
    val description: String
)