package com.ralphmarondev.pisync.navigation

import kotlinx.serialization.Serializable

object Routes {

    @Serializable
    data object Onboarding

    @Serializable
    data object Login

    @Serializable
    data object Home

    @Serializable
    data object About
}