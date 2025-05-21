package com.ralphmarondev.pisync.di

import com.ralphmarondev.pisync.core.di.coreModule
import com.ralphmarondev.pisync.features.app_theme.di.appThemeModule
import com.ralphmarondev.pisync.features.auth.di.authModule
import com.ralphmarondev.pisync.features.history.di.historyModule
import com.ralphmarondev.pisync.features.home.di.homeModule
import com.ralphmarondev.pisync.features.onboarding.di.onboardingModule
import com.ralphmarondev.pisync.features.overview.di.overviewModule
import com.ralphmarondev.pisync.features.privacy.di.privacyModule

val appModule = listOf(
    coreModule,
    authModule,
    homeModule,
    overviewModule,
    historyModule,
    appThemeModule,
    onboardingModule,
    privacyModule
)