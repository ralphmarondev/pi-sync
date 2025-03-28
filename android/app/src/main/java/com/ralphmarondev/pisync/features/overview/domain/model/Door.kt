package com.ralphmarondev.pisync.features.overview.domain.model

data class Door(
    val id: Int = -1,
    val name: String = "Add new room",
    val status: Boolean = false,
    val isActive: Boolean = true
)
