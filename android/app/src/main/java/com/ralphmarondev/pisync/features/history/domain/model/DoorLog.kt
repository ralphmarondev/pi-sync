package com.ralphmarondev.pisync.features.history.domain.model

data class DoorLog(
    val id: Int,
    val roomName: String?,
    val username: String,
    val description: String,
    val timestamp: String,
    val room: Int
)