package com.ralphmarondev.pisync.features.onboarding.di

import com.ralphmarondev.pisync.features.onboarding.presentation.OnboardingViewModel
import org.koin.androidx.viewmodel.dsl.viewModelOf
import org.koin.dsl.module

val onboardingModule = module {
    viewModelOf(::OnboardingViewModel)
}