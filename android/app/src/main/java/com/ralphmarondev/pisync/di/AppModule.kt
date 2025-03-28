package com.ralphmarondev.pisync.di

import com.ralphmarondev.pisync.core.di.coreModule
import com.ralphmarondev.pisync.features.auth.di.authModule
import com.ralphmarondev.pisync.features.home.di.homeModule
import com.ralphmarondev.pisync.features.overview.di.overviewModule

val appModule = listOf(
    coreModule,
    authModule,
    homeModule,
    overviewModule
)