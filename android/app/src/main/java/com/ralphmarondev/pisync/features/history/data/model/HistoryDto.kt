package com.ralphmarondev.pisync.features.history.data.model

import com.google.gson.annotations.SerializedName

data class HistoryDto(
    val id: Int,
    @SerializedName("room_name") val roomName: String,
    val username: String,
    val description: String,
    val timestamp: String,
    val room: Int
)
