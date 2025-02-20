package com.ralphmarondev.pisync.navigation

import kotlinx.serialization.Serializable

object Routes {

    @Serializable
    data object Onboarding

    @Serializable
    data object Auth

    @Serializable
    data object Home

    object HomeNav {
        @Serializable
        data object Dashboard

        @Serializable
        data object History

        @Serializable
        data object Settings
    }

    @Serializable
    data object About

    @Serializable
    data object Developer

    @Serializable
    data object Licenses
}