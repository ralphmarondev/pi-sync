package com.ralphmarondev.pisync.di

import com.ralphmarondev.pisync.core.di.coreModule
import com.ralphmarondev.pisync.features.auth.di.authModule

val appModule = listOf(
    coreModule,
    authModule
)