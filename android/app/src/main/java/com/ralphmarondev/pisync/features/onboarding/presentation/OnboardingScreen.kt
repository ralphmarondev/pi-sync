package com.ralphmarondev.pisync.features.onboarding.presentation

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.pager.HorizontalPager
import androidx.compose.foundation.pager.rememberPagerState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import coil.compose.rememberAsyncImagePainter
import com.ralphmarondev.pisync.R
import kotlinx.coroutines.delay

@Composable
fun OnboardingScreen(
    onCompleted: () -> Unit
) {
    val items = listOf(
        OnboardingItems(
            image = R.drawable.happy,
            title = stringResource(R.string.page1_title),
            description = stringResource(R.string.page1_description)
        ),
        OnboardingItems(
            image = R.drawable.happy,
            title = stringResource(R.string.page2_title),
            description = stringResource(R.string.page2_description)
        ),
        OnboardingItems(
            image = R.drawable.happy,
            title = stringResource(R.string.page3_title),
            description = stringResource(R.string.page3_description)
        )
    )
    val state = rememberPagerState { items.size }

    LaunchedEffect(state.currentPage) {
        while (true) {
            delay(3000)
            val nextPage = (state.currentPage + 1) % items.size
//            state.animateScrollToPage(nextPage)
            state.scrollToPage(nextPage)
        }
    }

    Scaffold { innerPadding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            HorizontalPager(
                state = state,
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp)
            ) {
                Box(
                    modifier = Modifier
                        .clip(RoundedCornerShape(16.dp))
                        .background(MaterialTheme.colorScheme.tertiaryContainer)
                        .fillMaxWidth()
                        .height(340.dp)
                        .padding(16.dp),
                    contentAlignment = Alignment.Center
                ) {
                    Image(
                        painter = rememberAsyncImagePainter(items[state.currentPage].image),
                        contentDescription = items[state.currentPage].title,
                        modifier = Modifier
                            .fillMaxHeight()
                            .fillMaxWidth()
                            .clip(RoundedCornerShape(8.dp)),
                        contentScale = ContentScale.Crop
                    )
                }
            }

            Text(
                text = items[state.currentPage].title,
                fontSize = 24.sp,
                fontWeight = FontWeight.W500,
                textAlign = TextAlign.Center,
                color = MaterialTheme.colorScheme.primary,
                modifier = Modifier.padding(horizontal = 16.dp),
                minLines = 2
            )
            Spacer(modifier = Modifier.height(4.dp))
            Text(
                text = items[state.currentPage].description,
                fontSize = 18.sp,
                fontWeight = FontWeight.W400,
                textAlign = TextAlign.Center,
                color = MaterialTheme.colorScheme.secondary,
                modifier = Modifier.padding(horizontal = 16.dp)
            )

            Spacer(modifier = Modifier.weight(1f))

            Row(
                modifier = Modifier.padding(8.dp),
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                repeat(items.size) { index ->
                    val color = when (state.currentPage == index) {
                        true -> MaterialTheme.colorScheme.primary
                        false -> MaterialTheme.colorScheme.tertiaryContainer
                    }
                    Box(
                        modifier = Modifier
                            .size(12.dp)
                            .clip(CircleShape)
                            .background(color)
                            .padding(2.dp)
                    )
                }
            }
            Spacer(modifier = Modifier.height(16.dp))

            Button(
                onClick = onCompleted,
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp)
            ) {
                Text(
                    text = "Get Started",
                    modifier = Modifier.padding(4.dp),
                    textAlign = TextAlign.Center,
                    fontSize = 18.sp,
                    fontWeight = FontWeight.W500
                )
            }
        }
    }
}

private data class OnboardingItems(
    val image: Int,
    val title: String,
    val description: String
)