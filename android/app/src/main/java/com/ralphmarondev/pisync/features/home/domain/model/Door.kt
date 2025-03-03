package com.ralphmarondev.pisync.features.home.domain.model

data class Door(
    val id: Int = 0,
    val label: String,
    val status: Boolean,
    val onClick: () -> Unit
)