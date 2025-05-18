package com.ralphmarondev.pisync.features.onboarding.presentation

import android.util.Log
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.rounded.ArrowForward
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.IconButtonDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import coil.compose.rememberAsyncImagePainter
import com.ralphmarondev.pisync.R
import com.ralphmarondev.pisync.features.onboarding.domain.model.Content
import com.ralphmarondev.pisync.features.onboarding.presentation.components.CompletedDialog
import org.koin.androidx.compose.koinViewModel

@Composable
fun OnboardingScreen(
    onboardingCompleted: () -> Unit
) {
    val viewModel: OnboardingViewModel = koinViewModel()
    val showCompletedDialog by viewModel.showCompletedDialog.collectAsState()
    val screenContentCount by viewModel.screenContentCount.collectAsState()

    val screenContent = listOf(
        Content(
            title = stringResource(R.string.title1),
            description = stringResource(R.string.description1),
            image = R.drawable.icpep_logo
        ),
        Content(
            title = stringResource(R.string.title2),
            description = stringResource(R.string.description2),
            image = R.drawable.icpep_coea_csu_logo
        ),
        Content(
            title = stringResource(R.string.title3),
            description = stringResource(R.string.description3),
            image = R.drawable.get_started
        )
    )

    Scaffold { innerPadding ->
        Column(
            modifier = Modifier
                .padding(innerPadding)
                .fillMaxSize(),
            verticalArrangement = Arrangement.SpaceBetween
        ) {
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .weight(1.5f)
                    .padding(16.dp)
                    .clip(RoundedCornerShape(8.dp))
                    .background(MaterialTheme.colorScheme.secondaryContainer),
                contentAlignment = Alignment.Center
            ) {
                Image(
                    painter = rememberAsyncImagePainter(screenContent[screenContentCount].image),
                    contentDescription = screenContent[screenContentCount].title,
                    modifier = Modifier
                        .size(200.dp),
                    contentScale = ContentScale.Crop
                )
            }

            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .weight(1f)
                    .padding(16.dp),
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center
            ) {
                Text(
                    text = screenContent[screenContentCount].title,
                    fontWeight = FontWeight.Bold,
                    fontSize = 24.sp,
                    color = MaterialTheme.colorScheme.primary,
                    textAlign = TextAlign.Center
                )
                Spacer(modifier = Modifier.height(8.dp))
                Text(
                    text = screenContent[screenContentCount].description,
                    fontWeight = FontWeight.W500,
                    fontSize = 18.sp,
                    color = MaterialTheme.colorScheme.secondary,
                    textAlign = TextAlign.Center
                )
                Spacer(modifier = Modifier.height(24.dp))
            }

            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp),
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.SpaceBetween
            ) {
                TextButton(
                    onClick = {
                        viewModel.showCompletedDialog()
                        Log.d("Onboarding", "Skipped.")
                    }
                ) {
                    Text(text = "Skip")
                }

                Row(
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    repeat(3) { index ->
                        val color =
                            if (screenContentCount == index) MaterialTheme.colorScheme.tertiary else MaterialTheme.colorScheme.primaryContainer
                        Box(
                            modifier = Modifier
                                .padding(4.dp)
                                .size(16.dp)
                                .clip(CircleShape)
                                .background(color)
                        )
                    }
                }

                IconButton(
                    onClick = {
                        Log.d("Onboarding", "Count: $screenContentCount")
                        if (screenContentCount < 2) {
                            viewModel.incrementScreenContentCount()
                        } else {
                            viewModel.showCompletedDialog()
                        }
                    },
                    modifier = Modifier.size(50.dp),
                    colors = IconButtonDefaults.iconButtonColors(
                        containerColor = Color.Green
                    )
                ) {
                    Icon(
                        imageVector = Icons.AutoMirrored.Rounded.ArrowForward,
                        contentDescription = "Next",
                        modifier = Modifier.size(30.dp)
                    )
                }
            }
        }

        if (showCompletedDialog) {
            CompletedDialog(
                onDismiss = {
                    viewModel.setOnboardingCompleted()
                    Log.d("Onboarding", "Completed.")
                    onboardingCompleted()
                }
            )
        }
    }
}