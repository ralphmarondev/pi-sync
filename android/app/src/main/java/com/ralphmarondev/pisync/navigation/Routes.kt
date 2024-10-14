package com.ralphmarondev.pisync.navigation

import kotlinx.serialization.Serializable

object Routes {
    @Serializable
    data object Auth

    @Serializable
    data object Home
}