package com.ralphmarondev.pisync.di

import com.ralphmarondev.pisync.core.di.coreModule
import com.ralphmarondev.pisync.features.auth.di.authModule
import com.ralphmarondev.pisync.features.home.di.homeModule

val appModule = listOf(
    coreModule,
    authModule,
    homeModule
)